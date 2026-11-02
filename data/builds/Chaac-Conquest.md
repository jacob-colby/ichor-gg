---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fulmination
  aspect_pick_rate: 0.22
  aspect_win_rate: 0.3
  slot_order:
  - name: Bancroft's Talon
    pick_rate: 0.2
    win_rate: 0.38
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.17
      win_rate: 0.25
    - name: Regrowth Striders
      pick_rate: 0.1
      win_rate: 0.56
  - name: Breastplate of Valor
    pick_rate: 0.19
    win_rate: 0.45
    alternates:
    - name: Brawler’s Beat Stick
      pick_rate: 0.11
      win_rate: 0.61
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.31
  - name: Freya's Tears
    pick_rate: 0.2
    win_rate: 0.48
    alternates:
    - name: Genji's Guard
      pick_rate: 0.19
      win_rate: 0.4
    - name: Regrowth Striders
      pick_rate: 0.06
      win_rate: 0.33
  - name: Gem of Focus
    pick_rate: 0.1
    win_rate: 0.44
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.41
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.47
  - name: Genji's Guard
    pick_rate: 0.1
    win_rate: 0.71
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.25
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.71
  - name: Soul Reaver
    pick_rate: 0.06
    win_rate: 0.57
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.43
    - name: Medallion
      pick_rate: 0.06
      win_rate: 0.67
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.48
    win_rate: 0.45
  - name: Bluestone Pendant
    pick_rate: 0.32
    win_rate: 0.3
  - name: Bumba's Hammer
    pick_rate: 0.06
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-10-30'
  god_win_rate: 0.40718562874251496
  god_matches_won: 68
  god_matches_played: 167
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-30'
  god_matches_analyzed: 10706
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Genji's Guard
  - Shield Splitter
  - Freya's Tears
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
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Gluttonous
    Grimoire, Shield Splitter, Spear of Desolation, Shifter''s Shield, Spear of the
    Magus, Runeforged Hammer, Helm of Radiance, Soul Gem, Berserker''s Shield, Obsidian
    Shard, Eye of the Storm, Erosion, Eye of Providence, Hydra''s Lament, Draconic
    Scale, Shield of the Phoenix, Rod of Asclepius, Stone of Binding, Heartseeker,
    Lotus Sickle, Jade Scepter, Magi''s Cloak, Avenging Blade, Doom Orb, Midgardian
    Mail, Helm of Darkness, Mantle Of Discord, Oni Hunter''s Garb, Wish-Granting Pearl,
    Screeching Gargoyle, Death Metal, Titan''s Bane, Daybreak Gavel, Chronos'' Pendant,
    The Crusher.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.52
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.55
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.71
      pick: 0.22
      fit: 0.24
    Shield Splitter:
      total: 0.5
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.48
      pick: 0.31
      fit: 0.4
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass,
    Spear of Desolation, Shield Splitter, Spear of the Magus, Hydra''s Lament, Helm
    of Radiance, Runeforged Hammer, Soul Gem, Lotus Sickle, Obsidian Shard, Shifter''s
    Shield, Heartseeker, Berserker''s Shield, Eye of the Storm, Rod of Asclepius,
    Doom Orb, Wish-Granting Pearl, The World Stone, Erosion, Shield of the Phoenix,
    Jade Scepter, Death Metal, Ancient Signet, Eye of Providence, Chronos'' Pendant,
    Avenging Blade, Stone of Binding, Draconic Scale, Oni Hunter''s Garb, Triton''s
    Conch, Helm of Darkness, Magi''s Cloak, Screeching Gargoyle, Titan''s Bane, The
    Crusher.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.52
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.46
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.71
      pick: 0.22
      fit: 0.29
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.48
      pick: 0.31
      fit: 0.35
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.85
      win: 0.52
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Genji's Guard
  - Transcendence
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Spear
    of Desolation, Kinetic Cuirass, Soul Gem, Spear of the Magus, Obsidian Shard,
    Shield Splitter, Helm of Radiance, Runeforged Hammer, Shifter''s Shield, Hydra''s
    Lament, Berserker''s Shield, Shield of the Phoenix, Lotus Sickle, Heartseeker,
    Eye of the Storm, Erosion, Doom Orb, Rod of Asclepius, Eye of Providence, Draconic
    Scale, Stone of Binding, The World Stone, Chronos'' Pendant, Screeching Gargoyle,
    Titan''s Bane, The Crusher, Dreamer''s Idol, Jade Scepter, Magi''s Cloak, Avenging
    Blade, The Reaper, Daybreak Gavel, Midgardian Mail, Wish-Granting Pearl, Oni Hunter''s
    Garb.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.5
      win: 0.52
      pick: 0.0
      fit: 0.14
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.52
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.71
      pick: 0.22
      fit: 0.27
    Transcendence:
      total: 0.44
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.14
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.85
      win: 0.52
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Genji's Guard
  - Runeforged Hammer
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Soul Gem, Rod of Asclepius,
    Shield of the Phoenix, Gluttonous Grimoire, Kinetic Cuirass, Ethereal Staff, The
    Reaper, Runeforged Hammer, Spear of Desolation, Spear of the Magus, Shield Splitter,
    Shifter''s Shield, Lifebinder, Berserker''s Shield, Obsidian Shard, Yogi''s Necklace,
    Helm of Radiance, Eye of the Storm, Sphere of Negation, Hydra''s Lament, Erosion,
    Phoenix Feather, Eye of Providence, Chandra''s Grace, Jade Scepter, Draconic Scale,
    Heartseeker, Blood-Bound Book, Avenging Blade, Lotus Sickle, Wish-Granting Pearl,
    Daybreak Gavel, Doom Orb, Stone of Binding, Midgardian Mail, Triton''s Conch.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.52
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.53
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.71
      pick: 0.22
      fit: 0.22
    Runeforged Hammer:
      total: 0.5
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.73
    Soul Gem:
      total: 0.53
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Genji's Guard
  - Transcendence
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire,
    Stone of Binding, Spear of Desolation, Spear of the Magus, Avenging Blade, Kinetic
    Cuirass, Screeching Gargoyle, Soul Gem, Obsidian Shard, Void Shield, Void Stone,
    Shield Splitter, Heartseeker, Runeforged Hammer, Helm of Radiance, Shifter''s
    Shield, Berserker''s Shield, Doom Orb, Titan''s Bane, The World Stone, The Crusher,
    Eye of the Storm, Dreamer''s Idol, Hydra''s Lament, Erosion, The Reaper, Eye of
    Providence, Rod of Asclepius, Shield of the Phoenix, Draconic Scale, Lotus Sickle,
    Jade Scepter, Magi''s Cloak, Daybreak Gavel, Midgardian Mail, Wish-Granting Pearl.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.5
      win: 0.52
      pick: 0.0
      fit: 0.13
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.52
      pick: 0.0
      fit: 0.49
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.71
      pick: 0.22
      fit: 0.21
    Transcendence:
      total: 0.44
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.14
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.85
      win: 0.52
      pick: 0.0
      fit: 0.4
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Nimble Ring
  - Gluttonous Grimoire
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge, Gluttonous Grimoire,
    Nimble Ring, Amanita Charm, Soul Gem, Kinetic Cuirass, Golden Blade, Spear of
    the Magus, Riptalon, Spear of Desolation, Helm of Radiance, Silverbranch Bow,
    Runeforged Hammer, Tyrfing, Shifter''s Shield, Obsidian Shard, Shield Splitter,
    Pharaoh''s Curse, Lernaean Bow, Toxic Blade, Shogun''s Ofuda, The Reaper, Rod
    of Asclepius, Hydra''s Lament, Erosion, Lotus Sickle, Stone of Binding, Shield
    of the Phoenix, Tekko-Kagi, Eye of Providence, Bragi''s Harp, Eye of the Storm,
    Bracer of The Abyss, Draconic Scale, Daybreak Gavel, Jade Scepter, Magi''s Cloak.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.45
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.37
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.71
      pick: 0.22
      fit: 0.17
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.69
      win: 0.52
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.33
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.6
      win: 0.52
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Spear of Desolation
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Spear of Desolation, Kinetic Cuirass, Soul Gem, Shield of the Phoenix,
    Hydra''s Lament, Gluttonous Grimoire, Lotus Sickle, Screeching Gargoyle, Shifter''s
    Shield, Berserker''s Shield, Chronos'' Pendant, Shield Splitter, Spear of the
    Magus, Helm of Radiance, Runeforged Hammer, Erosion, Prophetic Cloak, Obsidian
    Shard, Eye of Providence, Draconic Scale, Gladiator''s Shield, Stone of Binding,
    Eye of the Storm, Arondight, Rod of Asclepius, Magi''s Cloak, Midgardian Mail,
    Eye of Erebus, Daybreak Gavel, Oni Hunter''s Garb, Mantle Of Discord, Heartseeker,
    Pendulum Blade, Jade Scepter, Leviathan''s Hide.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.52
      pick: 0.0
      fit: 0.51
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.71
      pick: 0.22
      fit: 0.43
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.48
      pick: 0.31
      fit: 0.58
    Spear of Desolation:
      total: 0.51
      efficiency: 0.58
      win: 0.52
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.85
      win: 0.52
      pick: 0.0
      fit: 0.22
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Genji's Guard
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
    Cuirass, Gluttonous Grimoire, Shield Splitter, Spear of Desolation, Shifter''s
    Shield, Spear of the Magus, Runeforged Hammer, Helm of Radiance, Soul Gem, Berserker''s
    Shield, Obsidian Shard, Eye of the Storm, Erosion, Eye of Providence, Hydra''s
    Lament, Draconic Scale, Shield of the Phoenix, Rod of Asclepius, Stone of Binding,
    Heartseeker, Lotus Sickle, Jade Scepter, Magi''s Cloak, Avenging Blade, Doom Orb,
    Midgardian Mail, Helm of Darkness, Mantle Of Discord, Oni Hunter''s Garb, Wish-Granting
    Pearl, Screeching Gargoyle, Death Metal, Titan''s Bane, Daybreak Gavel, Chronos''
    Pendant, The Crusher.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.52
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.55
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.71
      pick: 0.22
      fit: 0.24
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.48
      pick: 0.31
      fit: 0.4
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.85
      win: 0.52
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
