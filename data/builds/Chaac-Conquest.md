---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fulmination
  aspect_pick_rate: 0.49
  aspect_win_rate: 0.46
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.6
    win_rate: 0.44
    alternates:
    - name: Transcendence
      pick_rate: 0.05
      win_rate: 0.6
    - name: Daybreak Gavel
      pick_rate: 0.04
      win_rate: 1.0
  - name: Sanguine Lash
    pick_rate: 0.34
    win_rate: 0.43
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.6
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.44
  - name: Umbral Link
    pick_rate: 0.13
    win_rate: 0.62
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.16
      win_rate: 0.63
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.45
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.69
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.63
    - name: Brawler’s Beat Stick
      pick_rate: 0.08
      win_rate: 0.63
  - name: Brawler’s Beat Stick
    pick_rate: 0.1
    win_rate: 0.33
    alternates:
    - name: Sundering Echo
      pick_rate: 0.07
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.8
  - name: Sundering Echo
    pick_rate: 0.08
    win_rate: 0.8
    alternates:
    - name: Contagion
      pick_rate: 0.06
      win_rate: 0.5
    - name: Sage's Ring
      pick_rate: 0.06
      win_rate: 0.75
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.5
    win_rate: 0.55
  - name: Bluestone Pendant
    pick_rate: 0.27
    win_rate: 0.39
  - name: Warrior's Axe
    pick_rate: 0.05
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-10-13'
  god_win_rate: 0.5
  god_matches_won: 51
  god_matches_played: 102
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-13'
  god_matches_analyzed: 7865
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Daybreak Gavel
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Daybreak Gavel, Genji''s Guard, Rod of Tahuti, Jotunn''s Revenge, Amanita
    Charm, Kinetic Cuirass, Breastplate of Valor, Gluttonous Grimoire, Shield Splitter,
    Spear of Desolation, Shifter''s Shield, Runeforged Hammer, Spear of the Magus,
    Helm of Radiance, Soul Gem, Berserker''s Shield, Obsidian Shard, Eye of the Storm,
    Erosion, Eye of Providence, Hydra''s Lament, Draconic Scale, Heartseeker, Shield
    of the Phoenix, Stone of Binding, Rod of Asclepius, Magi''s Cloak, Avenging Blade,
    Jade Scepter, Doom Orb, Screeching Gargoyle, Wish-Granting Pearl, Mantle Of Discord,
    Helm of Darkness, Midgardian Mail, Titan''s Bane, Death Metal, Chronos'' Pendant,
    The Crusher, The World Stone, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.8
      pick: 0.13
      fit: 0.24
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.55
    Daybreak Gavel:
      total: 0.68
      efficiency: 0.59
      win: 1.0
      pick: 0.04
      fit: 0.13
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.69
      pick: 0.23
      fit: 0.4
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Daybreak Gavel
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Daybreak Gavel
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Daybreak
    Gavel, Genji''s Guard, Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Breastplate
    of Valor, Gluttonous Grimoire, Kinetic Cuirass, Spear of Desolation, Shield Splitter,
    Spear of the Magus, Hydra''s Lament, Runeforged Hammer, Helm of Radiance, Soul
    Gem, Obsidian Shard, Heartseeker, Berserker''s Shield, Shifter''s Shield, Eye
    of the Storm, Rod of Asclepius, Wish-Granting Pearl, Doom Orb, Ancient Signet,
    The World Stone, Shield of the Phoenix, Erosion, Death Metal, Chronos'' Pendant,
    Jade Scepter, Stone of Binding, Eye of Providence, Avenging Blade, Draconic Scale,
    Screeching Gargoyle, Magi''s Cloak, Titan''s Bane, Helm of Darkness, Triton''s
    Conch, The Crusher, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.8
      pick: 0.13
      fit: 0.29
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.45
    Daybreak Gavel:
      total: 0.67
      efficiency: 0.59
      win: 1.0
      pick: 0.04
      fit: 0.1
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.69
      pick: 0.23
      fit: 0.35
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.62
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Daybreak Gavel
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Daybreak Gavel
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Daybreak Gavel, Genji''s Guard, Rod of Tahuti, Jotunn''s Revenge, Amanita
    Charm, Breastplate of Valor, Gluttonous Grimoire, Spear of Desolation, Kinetic
    Cuirass, Soul Gem, Spear of the Magus, Obsidian Shard, Shield Splitter, Runeforged
    Hammer, Helm of Radiance, Shifter''s Shield, Berserker''s Shield, Hydra''s Lament,
    Heartseeker, Shield of the Phoenix, Eye of the Storm, Erosion, Doom Orb, Rod of
    Asclepius, Eye of Providence, Screeching Gargoyle, Stone of Binding, Chronos''
    Pendant, Draconic Scale, The World Stone, Titan''s Bane, The Crusher, Dreamer''s
    Idol, Magi''s Cloak, Jade Scepter, The Reaper, Wish-Granting Pearl, Avenging Blade,
    Mantle Of Discord, Midgardian Mail, Ancient Signet.'
  slot_scores:
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.8
      pick: 0.13
      fit: 0.27
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.63
      pick: 0.13
      fit: 0.27
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.48
    Daybreak Gavel:
      total: 0.68
      efficiency: 0.59
      win: 1.0
      pick: 0.04
      fit: 0.11
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.69
      pick: 0.23
      fit: 0.41
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Daybreak Gavel
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Daybreak Gavel
  - Freya's Tears
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Daybreak Gavel, Genji''s Guard, Rod of Tahuti, Amanita Charm, Jotunn''s
    Revenge, Soul Gem, Rod of Asclepius, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Breastplate of Valor, Ethereal Staff, The Reaper, Runeforged
    Hammer, Spear of Desolation, Spear of the Magus, Shield Splitter, Shifter''s Shield,
    Berserker''s Shield, Lifebinder, Obsidian Shard, Helm of Radiance, Eye of the
    Storm, Yogi''s Necklace, Sphere of Negation, Hydra''s Lament, Erosion, Heartseeker,
    Phoenix Feather, Eye of Providence, Chandra''s Grace, Draconic Scale, Avenging
    Blade, Blood-Bound Book, Jade Scepter, Wish-Granting Pearl, Stone of Binding,
    Doom Orb, Glorious Pridwen, Midgardian Mail, Titan''s Bane.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.8
      pick: 0.13
      fit: 0.22
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.42
    Daybreak Gavel:
      total: 0.68
      efficiency: 0.59
      win: 1.0
      pick: 0.04
      fit: 0.16
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.69
      pick: 0.23
      fit: 0.35
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.73
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Genji's Guard
  - Daybreak Gavel
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Jotunn's Revenge
  - Daybreak Gavel
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Daybreak Gavel, Rod of Tahuti, Genji''s Guard, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Stone of Binding, Spear of Desolation, Spear
    of the Magus, Breastplate of Valor, Avenging Blade, Kinetic Cuirass, Screeching
    Gargoyle, Soul Gem, Obsidian Shard, Void Shield, Heartseeker, Void Stone, Shield
    Splitter, Runeforged Hammer, Helm of Radiance, Shifter''s Shield, Berserker''s
    Shield, Doom Orb, Titan''s Bane, The Crusher, The World Stone, Eye of the Storm,
    Hydra''s Lament, Dreamer''s Idol, Erosion, The Reaper, Eye of Providence, Rod
    of Asclepius, Shield of the Phoenix, Draconic Scale, Magi''s Cloak, Jade Scepter,
    Wish-Granting Pearl, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Stone of Binding:
      total: 0.56
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.67
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.8
      pick: 0.13
      fit: 0.21
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.49
    Daybreak Gavel:
      total: 0.68
      efficiency: 0.59
      win: 1.0
      pick: 0.04
      fit: 0.11
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.69
      pick: 0.23
      fit: 0.34
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Daybreak Gavel
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Daybreak Gavel
  - Nimble Ring
  - Freya's Tears
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Daybreak Gavel, Genji''s Guard, Rod of Tahuti, Berserker''s Shield,
    Jotunn''s Revenge, Gluttonous Grimoire, Nimble Ring, Amanita Charm, Breastplate
    of Valor, Soul Gem, Kinetic Cuirass, Golden Blade, Riptalon, Spear of the Magus,
    Spear of Desolation, Silverbranch Bow, Helm of Radiance, Runeforged Hammer, Tyrfing,
    Shield Splitter, Shifter''s Shield, Obsidian Shard, Lernaean Bow, Pharaoh''s Curse,
    Toxic Blade, Shogun''s Ofuda, The Reaper, Rod of Asclepius, Hydra''s Lament, Stone
    of Binding, Erosion, Tekko-Kagi, Bragi''s Harp, Shield of the Phoenix, Eye of
    Providence, Eye of the Storm, Bracer of The Abyss, Heartseeker, Draconic Scale,
    Magi''s Cloak, Screeching Gargoyle.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.62
      efficiency: 0.66
      win: 0.8
      pick: 0.13
      fit: 0.17
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.37
    Daybreak Gavel:
      total: 0.67
      efficiency: 0.59
      win: 1.0
      pick: 0.04
      fit: 0.09
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.33
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.69
      pick: 0.23
      fit: 0.28
  community_ordered:
  - Genji's Guard
  - Daybreak Gavel
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Daybreak Gavel
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Daybreak Gavel, Genji''s Guard, Rod
    of Tahuti, Jotunn''s Revenge, Breastplate of Valor, Amanita Charm, Spear of Desolation,
    Kinetic Cuirass, Soul Gem, Shield of the Phoenix, Hydra''s Lament, Screeching
    Gargoyle, Gluttonous Grimoire, Shifter''s Shield, Berserker''s Shield, Chronos''
    Pendant, Shield Splitter, Spear of the Magus, Runeforged Hammer, Helm of Radiance,
    Prophetic Cloak, Erosion, Obsidian Shard, Eye of Providence, Stone of Binding,
    Draconic Scale, Gladiator''s Shield, Eye of the Storm, Arondight, Gem of Focus,
    Magi''s Cloak, Rod of Asclepius, Heartseeker, Eye of Erebus, Mantle Of Discord,
    Midgardian Mail, Pendulum Blade, Hide of the Nemean Lion, Glorious Pridwen, Jade
    Scepter, Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.66
      efficiency: 0.66
      win: 0.8
      pick: 0.13
      fit: 0.43
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.13
      fit: 0.43
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.51
    Daybreak Gavel:
      total: 0.68
      efficiency: 0.59
      win: 1.0
      pick: 0.04
      fit: 0.12
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.69
      pick: 0.23
      fit: 0.58
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Daybreak Gavel
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Kinetic
    Cuirass, Gluttonous Grimoire, Genji''s Guard, Shield Splitter, Breastplate of
    Valor, Shifter''s Shield, Spear of Desolation, Runeforged Hammer, Spear of the
    Magus, Helm of Radiance, Soul Gem, Berserker''s Shield, Obsidian Shard, Eye of
    the Storm, Erosion, Eye of Providence, Hydra''s Lament, Draconic Scale, Heartseeker,
    Shield of the Phoenix, Stone of Binding, Rod of Asclepius, Magi''s Cloak, Avenging
    Blade, Jade Scepter, Doom Orb, Screeching Gargoyle, Wish-Granting Pearl, Mantle
    Of Discord, Helm of Darkness, Midgardian Mail, Titan''s Bane, Death Metal, Chronos''
    Pendant, The Crusher, Daybreak Gavel, The World Stone, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.8
      pick: 0.13
      fit: 0.24
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.69
      pick: 0.23
      fit: 0.4
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.62
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
