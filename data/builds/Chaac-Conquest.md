---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fulmination
  aspect_pick_rate: 0.33
  aspect_win_rate: 0.19
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.25
    win_rate: 0.25
    alternates:
    - name: Regrowth Striders
      pick_rate: 0.19
      win_rate: 0.5
    - name: Bancroft's Talon
      pick_rate: 0.11
      win_rate: 0.14
  - name: Brawler’s Beat Stick
    pick_rate: 0.2
    win_rate: 0.62
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.14
      win_rate: 0.44
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.43
  - name: Genji's Guard
    pick_rate: 0.31
    win_rate: 0.47
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.33
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.4
  - name: Glorious Pridwen
    pick_rate: 0.17
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.67
    - name: Brawler’s Beat Stick
      pick_rate: 0.08
      win_rate: 0.4
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.71
    alternates:
    - name: Sundering Echo
      pick_rate: 0.06
      win_rate: 0.67
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.33
  - name: Sundering Echo
    pick_rate: 0.11
    win_rate: 0.25
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.5
    - name: Captain's Ring
      pick_rate: 0.05
      win_rate: 0.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.53
    win_rate: 0.41
  - name: Bluestone Pendant
    pick_rate: 0.38
    win_rate: 0.25
  - name: Archmage's Gem
    pick_rate: 0.02
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-10-24'
  god_win_rate: 0.359375
  god_matches_won: 23
  god_matches_played: 64
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-24'
  god_matches_analyzed: 3785
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Jotunn's Revenge
  - Shell of Rebuke
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Brawler’s Beat Stick
  - Shell of Rebuke
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Gluttonous
    Grimoire, Shield Splitter, Spear of Desolation, Runeforged Hammer, Spear of the
    Magus, Helm of Radiance, Soul Gem, Berserker''s Shield, Obsidian Shard, Eye of
    the Storm, Shifter''s Shield, Erosion, Eye of Providence, Hydra''s Lament, Draconic
    Scale, Heartseeker, Shield of the Phoenix, Stone of Binding, Rod of Asclepius,
    Magi''s Cloak, Avenging Blade, Jade Scepter, Doom Orb, Screeching Gargoyle, Wish-Granting
    Pearl, Mantle Of Discord, Helm of Darkness, Midgardian Mail, Titan''s Bane, Death
    Metal, Chronos'' Pendant, The Crusher, Daybreak Gavel, The World Stone, Hide of
    the Nemean Lion.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.49
      efficiency: 0.42
      win: 0.62
      pick: 0.27
      fit: 0.32
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.47
      pick: 0.48
      fit: 0.24
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.44
      pick: 0.0
      fit: 0.4
    Shell of Rebuke:
      total: 0.48
      efficiency: 0.28
      win: 0.71
      pick: 0.28
      fit: 0.32
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.34
      fit: 0.4
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: mana-stack
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Brawler’s Beat Stick
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass,
    Spear of Desolation, Shield Splitter, Spear of the Magus, Hydra''s Lament, Runeforged
    Hammer, Helm of Radiance, Soul Gem, Obsidian Shard, Heartseeker, Berserker''s
    Shield, Eye of the Storm, Rod of Asclepius, Wish-Granting Pearl, Doom Orb, Ancient
    Signet, Shifter''s Shield, The World Stone, Shield of the Phoenix, Erosion, Death
    Metal, Chronos'' Pendant, Jade Scepter, Stone of Binding, Eye of Providence, Avenging
    Blade, Draconic Scale, Screeching Gargoyle, Magi''s Cloak, Titan''s Bane, Helm
    of Darkness, Triton''s Conch, The Crusher, Daybreak Gavel, Oni Hunter''s Garb.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.48
      efficiency: 0.42
      win: 0.62
      pick: 0.27
      fit: 0.26
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.47
      pick: 0.48
      fit: 0.29
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.44
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.34
      fit: 0.35
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.44
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Jotunn's Revenge
  - Shell of Rebuke
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Brawler’s Beat Stick
  - Shell of Rebuke
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Spear
    of Desolation, Kinetic Cuirass, Soul Gem, Spear of the Magus, Obsidian Shard,
    Shield Splitter, Runeforged Hammer, Helm of Radiance, Berserker''s Shield, Hydra''s
    Lament, Heartseeker, Shield of the Phoenix, Shifter''s Shield, Eye of the Storm,
    Erosion, Doom Orb, Rod of Asclepius, Eye of Providence, Screeching Gargoyle, Stone
    of Binding, Chronos'' Pendant, Draconic Scale, The World Stone, Titan''s Bane,
    The Crusher, Dreamer''s Idol, Magi''s Cloak, Jade Scepter, The Reaper, Wish-Granting
    Pearl, Avenging Blade, Daybreak Gavel, Mantle Of Discord, Midgardian Mail, Ancient
    Signet.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.48
      efficiency: 0.42
      win: 0.62
      pick: 0.27
      fit: 0.27
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.47
      pick: 0.48
      fit: 0.27
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.44
      pick: 0.0
      fit: 0.48
    Shell of Rebuke:
      total: 0.47
      efficiency: 0.28
      win: 0.71
      pick: 0.28
      fit: 0.27
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.34
      fit: 0.41
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Jotunn's Revenge
  - Glorious Pridwen
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Brawler’s Beat Stick
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
    this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Soul Gem, Rod of Asclepius,
    Shield of the Phoenix, Gluttonous Grimoire, Kinetic Cuirass, Ethereal Staff, The
    Reaper, Runeforged Hammer, Spear of Desolation, Spear of the Magus, Shield Splitter,
    Berserker''s Shield, Lifebinder, Obsidian Shard, Helm of Radiance, Eye of the
    Storm, Yogi''s Necklace, Sphere of Negation, Shifter''s Shield, Hydra''s Lament,
    Erosion, Heartseeker, Phoenix Feather, Eye of Providence, Chandra''s Grace, Draconic
    Scale, Avenging Blade, Blood-Bound Book, Jade Scepter, Wish-Granting Pearl, Stone
    of Binding, Daybreak Gavel, Doom Orb, Midgardian Mail, Titan''s Bane.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.48
      efficiency: 0.42
      win: 0.62
      pick: 0.27
      fit: 0.26
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.47
      pick: 0.48
      fit: 0.22
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.44
      pick: 0.0
      fit: 0.42
    Glorious Pridwen:
      total: 0.51
      efficiency: 0.38
      win: 0.6
      pick: 0.28
      fit: 0.65
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.34
      fit: 0.35
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.73
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Glorious Pridwen
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Brawler’s Beat Stick
  - Stone of Binding
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Brawler’s Beat Stick
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Glorious Pridwen — physical protection
    swap_item: Glorious Pridwen
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire,
    Stone of Binding, Spear of Desolation, Spear of the Magus, Avenging Blade, Kinetic
    Cuirass, Screeching Gargoyle, Soul Gem, Obsidian Shard, Void Shield, Heartseeker,
    Void Stone, Shield Splitter, Runeforged Hammer, Helm of Radiance, Berserker''s
    Shield, Doom Orb, Titan''s Bane, The Crusher, The World Stone, Eye of the Storm,
    Shifter''s Shield, Hydra''s Lament, Dreamer''s Idol, Erosion, The Reaper, Eye
    of Providence, Rod of Asclepius, Shield of the Phoenix, Draconic Scale, Magi''s
    Cloak, Jade Scepter, Daybreak Gavel, Wish-Granting Pearl, Mantle Of Discord, Midgardian
    Mail.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.48
      efficiency: 0.42
      win: 0.62
      pick: 0.27
      fit: 0.27
    Stone of Binding:
      total: 0.48
      efficiency: 0.51
      win: 0.44
      pick: 0.0
      fit: 0.67
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.47
      pick: 0.48
      fit: 0.21
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.44
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.34
      fit: 0.34
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
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
    swap: Brawler’s Beat Stick — physical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge, Gluttonous Grimoire,
    Nimble Ring, Amanita Charm, Soul Gem, Kinetic Cuirass, Golden Blade, Riptalon,
    Spear of the Magus, Spear of Desolation, Silverbranch Bow, Helm of Radiance, Runeforged
    Hammer, Tyrfing, Shield Splitter, Obsidian Shard, Lernaean Bow, Pharaoh''s Curse,
    Toxic Blade, Shogun''s Ofuda, The Reaper, Shifter''s Shield, Rod of Asclepius,
    Hydra''s Lament, Stone of Binding, Erosion, Tekko-Kagi, Bragi''s Harp, Shield
    of the Phoenix, Eye of Providence, Eye of the Storm, Bracer of The Abyss, Heartseeker,
    Draconic Scale, Daybreak Gavel, Magi''s Cloak, Screeching Gargoyle.'
  slot_scores:
    Golden Blade:
      total: 0.45
      efficiency: 0.52
      win: 0.44
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.47
      pick: 0.48
      fit: 0.17
    Berserker's Shield:
      total: 0.49
      efficiency: 0.68
      win: 0.44
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.72
      win: 0.44
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.47
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.33
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.34
      fit: 0.28
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Glorious Pridwen
  - Freya's Tears
  flex_slots:
  - Breastplate of Valor
  - Brawler’s Beat Stick
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shell of Rebuke — physical protection
    swap_item: Shell of Rebuke
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Spear of Desolation, Kinetic Cuirass, Soul Gem, Shield of the Phoenix,
    Hydra''s Lament, Screeching Gargoyle, Gluttonous Grimoire, Berserker''s Shield,
    Chronos'' Pendant, Shield Splitter, Spear of the Magus, Runeforged Hammer, Helm
    of Radiance, Shifter''s Shield, Prophetic Cloak, Erosion, Obsidian Shard, Eye
    of Providence, Stone of Binding, Draconic Scale, Gladiator''s Shield, Eye of the
    Storm, Arondight, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Heartseeker,
    Eye of Erebus, Mantle Of Discord, Daybreak Gavel, Midgardian Mail, Pendulum Blade,
    Hide of the Nemean Lion, Jade Scepter, Chandra''s Grace.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.48
      efficiency: 0.42
      win: 0.62
      pick: 0.27
      fit: 0.29
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.47
      pick: 0.48
      fit: 0.43
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.43
      pick: 0.15
      fit: 0.43
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.44
      pick: 0.0
      fit: 0.51
    Glorious Pridwen:
      total: 0.5
      efficiency: 0.38
      win: 0.6
      pick: 0.28
      fit: 0.58
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.34
      fit: 0.58
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Breastplate of Valor
  - Glorious Pridwen
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
    Cuirass, Gluttonous Grimoire, Shield Splitter, Shifter''s Shield, Spear of Desolation,
    Runeforged Hammer, Spear of the Magus, Helm of Radiance, Soul Gem, Berserker''s
    Shield, Obsidian Shard, Eye of the Storm, Erosion, Eye of Providence, Hydra''s
    Lament, Draconic Scale, Heartseeker, Shield of the Phoenix, Stone of Binding,
    Rod of Asclepius, Magi''s Cloak, Avenging Blade, Jade Scepter, Doom Orb, Screeching
    Gargoyle, Wish-Granting Pearl, Mantle Of Discord, Helm of Darkness, Midgardian
    Mail, Titan''s Bane, Death Metal, Chronos'' Pendant, The Crusher, Daybreak Gavel,
    The World Stone, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.47
      pick: 0.48
      fit: 0.24
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.44
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.56
      win: 0.44
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.34
      fit: 0.4
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.44
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.44
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
