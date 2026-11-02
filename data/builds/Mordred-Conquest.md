---
type: smite-build
god: Mordred
mode: Conquest
builds:
- source: community
  aspect: Aspect of Rage
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.47
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.33
    win_rate: 0.49
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.31
      win_rate: 0.51
    - name: Bracer of The Abyss
      pick_rate: 0.1
      win_rate: 0.55
  - name: Sanguine Lash
    pick_rate: 0.15
    win_rate: 0.55
    alternates:
    - name: Shield of the Phoenix
      pick_rate: 0.1
      win_rate: 0.41
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.54
  - name: Nimble Ring
    pick_rate: 0.11
    win_rate: 0.62
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.1
      win_rate: 0.48
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.51
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.54
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.6
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.58
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.39
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.66
    - name: Draconic Scale
      pick_rate: 0.06
      win_rate: 0.73
  - name: Medal of Defense
    pick_rate: 0.07
    win_rate: 0.38
    alternates:
    - name: Killing Stone
      pick_rate: 0.05
      win_rate: 0.67
    - name: Hide of the Nemean Lion
      pick_rate: 0.04
      win_rate: 0.64
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.37
    win_rate: 0.61
  - name: Bluestone Pendant
    pick_rate: 0.24
    win_rate: 0.33
  - name: Leather Cowl
    pick_rate: 0.16
    win_rate: 0.48
  source_url: https://smitebrain.com/gods/mordred/
  last_verified: '2026-10-30'
  god_win_rate: 0.5245901639344263
  god_matches_won: 224
  god_matches_played: 427
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-30'
  god_matches_analyzed: 10706
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Kinetic Cuirass, Jotunn''s Revenge, Amanita Charm, Shield
    Splitter, Breastplate of Valor, Genji''s Guard, Runeforged Hammer, Eye of the
    Storm, Gluttonous Grimoire, Berserker''s Shield, Erosion, Eye of Providence, Hydra''s
    Lament, Stone of Binding, Spear of Desolation, Helm of Radiance, Spear of the
    Magus, Heartseeker, Magi''s Cloak, Soul Gem, Avenging Blade, Midgardian Mail,
    Obsidian Shard, Mantle Of Discord, Oni Hunter''s Garb, Screeching Gargoyle, Titan''s
    Bane, Leviathan''s Hide, Daybreak Gavel, The Crusher, Void Shield, Ancile, Rod
    of Asclepius, Stampede, Spectral Armor, The Reaper, Shield of the Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.57
      win: 0.58
      pick: 0.1
      fit: 0.61
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.54
      pick: 0.27
      fit: 0.47
    Draconic Scale:
      total: 0.59
      efficiency: 0.5
      win: 0.73
      pick: 0.13
      fit: 0.51
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Draconic
    Scale, Jotunn''s Revenge, Kinetic Cuirass, Amanita Charm, Breastplate of Valor,
    Gluttonous Grimoire, Genji''s Guard, Spear of Desolation, Shield Splitter, Spear
    of the Magus, Hydra''s Lament, Helm of Radiance, Runeforged Hammer, Soul Gem,
    Lotus Sickle, Obsidian Shard, Heartseeker, Berserker''s Shield, Eye of the Storm,
    Rod of Asclepius, Doom Orb, Wish-Granting Pearl, The World Stone, Erosion, Jade
    Scepter, Death Metal, Ancient Signet, Eye of Providence, Chronos'' Pendant, Avenging
    Blade, Stone of Binding, Oni Hunter''s Garb, Triton''s Conch, Helm of Darkness,
    Magi''s Cloak, Screeching Gargoyle, Titan''s Bane, The Crusher, Shield of the
    Phoenix.'
  slot_scores:
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.57
      win: 0.58
      pick: 0.1
      fit: 0.46
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.73
      pick: 0.13
      fit: 0.36
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.85
      win: 0.6
      pick: 0.17
      fit: 0.36
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Draconic Scale, Jotunn''s Revenge, Kinetic Cuirass, Amanita Charm, Gluttonous
    Grimoire, Spear of Desolation, Soul Gem, Breastplate of Valor, Spear of the Magus,
    Genji''s Guard, Obsidian Shard, Shield Splitter, Helm of Radiance, Runeforged
    Hammer, Hydra''s Lament, Berserker''s Shield, Lotus Sickle, Heartseeker, Eye of
    the Storm, Erosion, Doom Orb, Rod of Asclepius, Eye of Providence, Stone of Binding,
    The World Stone, Chronos'' Pendant, Screeching Gargoyle, Titan''s Bane, The Crusher,
    Dreamer''s Idol, Jade Scepter, Magi''s Cloak, Avenging Blade, The Reaper, Daybreak
    Gavel, Midgardian Mail, Wish-Granting Pearl, Oni Hunter''s Garb, Shield of the
    Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.1
      fit: 0.48
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.27
      fit: 0.41
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.73
      pick: 0.13
      fit: 0.38
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.85
      win: 0.6
      pick: 0.17
      fit: 0.34
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Draconic Scale, Jotunn''s Revenge, Kinetic Cuirass, Soul
    Gem, Rod of Asclepius, The Reaper, Runeforged Hammer, Shield Splitter, Gluttonous
    Grimoire, Breastplate of Valor, Eye of the Storm, Berserker''s Shield, Genji''s
    Guard, Ethereal Staff, Yogi''s Necklace, Erosion, Eye of Providence, Hydra''s
    Lament, Phoenix Feather, Chandra''s Grace, Spear of Desolation, Avenging Blade,
    Shield of the Phoenix, Heartseeker, Spear of the Magus, Lifebinder, Helm of Radiance,
    Midgardian Mail, Glorious Pridwen, Stone of Binding, Obsidian Shard, Oni Hunter''s
    Garb, Daybreak Gavel, Sphere of Negation, Titan''s Bane, Leviathan''s Hide, The
    Crusher.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.1
      fit: 0.6
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.73
      pick: 0.13
      fit: 0.5
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.85
      win: 0.6
      pick: 0.17
      fit: 0.2
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.53
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Draconic Scale, Jotunn''s Revenge, Kinetic Cuirass, Amanita Charm,
    Stone of Binding, Gluttonous Grimoire, Avenging Blade, Screeching Gargoyle, Void
    Shield, Spear of Desolation, Spear of the Magus, Breastplate of Valor, Shield
    Splitter, Void Stone, Heartseeker, Soul Gem, Obsidian Shard, Genji''s Guard, Runeforged
    Hammer, Berserker''s Shield, Titan''s Bane, The Crusher, Eye of the Storm, Erosion,
    The Reaper, Hydra''s Lament, Eye of Providence, Helm of Radiance, Doom Orb, The
    World Stone, Magi''s Cloak, Dreamer''s Idol, Pendulum Blade, Midgardian Mail,
    Daybreak Gavel, Oni Hunter''s Garb, Avatar''s Parashu, Mantle Of Discord, Shield
    of the Phoenix.'
  slot_scores:
    Stone of Binding:
      total: 0.53
      efficiency: 0.5
      win: 0.55
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.1
      fit: 0.52
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.27
      fit: 0.38
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.73
      pick: 0.13
      fit: 0.42
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Nimble Ring
  - Draconic Scale
  flex_slots:
  - Jotunn's Revenge
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Berserker''s Shield, Kinetic Cuirass, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Golden Blade, Breastplate of Valor, Soul Gem,
    Genji''s Guard, Riptalon, Tyrfing, Silverbranch Bow, Shield Splitter, Runeforged
    Hammer, Pharaoh''s Curse, Toxic Blade, Lernaean Bow, Shogun''s Ofuda, Helm of
    Radiance, Spear of the Magus, Erosion, Spear of Desolation, Hydra''s Lament, The
    Reaper, Eye of Providence, Stone of Binding, Eye of the Storm, Tekko-Kagi, Obsidian
    Shard, Daybreak Gavel, Magi''s Cloak, Midgardian Mail, Screeching Gargoyle, Heartseeker,
    Rod of Asclepius, Oni Hunter''s Garb, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.5
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.57
      win: 0.58
      pick: 0.1
      fit: 0.44
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.17
      fit: 0.28
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.73
      pick: 0.13
      fit: 0.34
  community_ordered:
  - Kinetic Cuirass
  - Nimble Ring
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Draconic Scale, Jotunn''s Revenge,
    Kinetic Cuirass, Breastplate of Valor, Amanita Charm, Genji''s Guard, Spear of
    Desolation, Soul Gem, Hydra''s Lament, Lotus Sickle, Screeching Gargoyle, Gluttonous
    Grimoire, Chronos'' Pendant, Berserker''s Shield, Shield Splitter, Helm of Radiance,
    Spear of the Magus, Runeforged Hammer, Erosion, Prophetic Cloak, Eye of Providence,
    Obsidian Shard, Gladiator''s Shield, Stone of Binding, Eye of the Storm, Gem of
    Focus, Arondight, Rod of Asclepius, Magi''s Cloak, Eye of Erebus, Midgardian Mail,
    Daybreak Gavel, Oni Hunter''s Garb, Mantle Of Discord, Jade Scepter, Pendulum
    Blade, Chandra''s Grace, Heartseeker, Shield of the Phoenix.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.1
      fit: 0.51
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.54
      pick: 0.27
      fit: 0.59
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.73
      pick: 0.13
      fit: 0.41
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Draconic Scale, Jotunn''s Revenge, Kinetic
    Cuirass, Amanita Charm, Gluttonous Grimoire, Spear of Desolation, Soul Gem, Spear
    of the Magus, Breastplate of Valor, Helm of Radiance, Genji''s Guard, Obsidian
    Shard, Shield Splitter, Runeforged Hammer, Lotus Sickle, Rod of Asclepius, Berserker''s
    Shield, Hydra''s Lament, Eye of the Storm, Jade Scepter, Chronos'' Pendant, Erosion,
    Doom Orb, Eye of Providence, Wish-Granting Pearl, The World Stone, Stone of Binding,
    Death Metal, Heartseeker, Helm of Darkness, Dreamer''s Idol, Screeching Gargoyle,
    Ancient Signet, Magi''s Cloak, Avenging Blade, Ethereal Staff, Triton''s Conch,
    Daybreak Gavel, Shield of the Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.1
      fit: 0.49
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.27
      fit: 0.39
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.73
      pick: 0.13
      fit: 0.39
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.85
      win: 0.6
      pick: 0.17
      fit: 0.35
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Freya's Tears
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Draconic Scale, Jotunn''s Revenge,
    Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire, Spear of Desolation, Shield
    Splitter, Spear of the Magus, Breastplate of Valor, Helm of Radiance, Soul Gem,
    Runeforged Hammer, Obsidian Shard, Genji''s Guard, Berserker''s Shield, Eye of
    the Storm, Hydra''s Lament, Rod of Asclepius, Erosion, Eye of Providence, Lotus
    Sickle, Heartseeker, Jade Scepter, Stone of Binding, Doom Orb, Death Metal, Avenging
    Blade, Wish-Granting Pearl, The World Stone, Magi''s Cloak, Chronos'' Pendant,
    Helm of Darkness, Titan''s Bane, The Crusher, Dreamer''s Idol, Triton''s Conch,
    Midgardian Mail, Daybreak Gavel, Shield of the Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.1
      fit: 0.52
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.27
      fit: 0.38
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.73
      pick: 0.13
      fit: 0.42
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.85
      win: 0.6
      pick: 0.17
      fit: 0.33
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Shield
    Splitter, Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Eye of the
    Storm, Gluttonous Grimoire, Berserker''s Shield, Erosion, Eye of Providence, Draconic
    Scale, Shield of the Phoenix, Hydra''s Lament, Stone of Binding, Spear of Desolation,
    Helm of Radiance, Spear of the Magus, Heartseeker, Magi''s Cloak, Soul Gem, Avenging
    Blade, Midgardian Mail, Obsidian Shard, Mantle Of Discord, Oni Hunter''s Garb,
    Screeching Gargoyle, Titan''s Bane, Leviathan''s Hide, Daybreak Gavel, The Crusher,
    Void Shield, Ancile, Rod of Asclepius, Stampede, Spectral Armor, The Reaper.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.51
      pick: 0.12
      fit: 0.28
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.55
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.57
      win: 0.58
      pick: 0.1
      fit: 0.61
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.54
      pick: 0.27
      fit: 0.47
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
