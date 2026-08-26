---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.18
  aspect_win_rate: 0.5
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.45
    win_rate: 0.3
    alternates:
    - name: Mystical Mail
      pick_rate: 0.14
      win_rate: 1.0
    - name: Book of Thoth
      pick_rate: 0.14
      win_rate: 0.33
  - name: Gladiator's Shield
    pick_rate: 0.14
    win_rate: 0.33
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 1.0
    - name: Ancient Signet
      pick_rate: 0.14
      win_rate: 0.33
  - name: Genji's Guard
    pick_rate: 0.23
    win_rate: 0.4
    alternates:
    - name: Soul Reaver
      pick_rate: 0.09
      win_rate: 1.0
    - name: Gladiator's Shield
      pick_rate: 0.09
      win_rate: 0.0
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.0
    - name: Gem of Focus
      pick_rate: 0.1
      win_rate: 0.5
  - name: Draconic Scale
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.15
      win_rate: 0.33
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.5
  - name: Void Shard
    pick_rate: 0.13
    win_rate: 0.0
    alternates:
    - name: Sundering Echo
      pick_rate: 0.13
      win_rate: 0.5
    - name: Runeforged Hammer
      pick_rate: 0.07
      win_rate: 0.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.45
    win_rate: 0.6
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.75
  - name: Conduit Gem
    pick_rate: 0.14
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-08-26'
  god_win_rate: 0.45454545454545453
  god_matches_won: 10
  god_matches_played: 22
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Mystical Mail
  - Freya's Tears
  - Soul Reaver
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Berserker''s Shield, Amanita Charm, Kinetic Cuirass,
    Shield Splitter, Eye of the Storm, Avenging Blade, Gluttonous Grimoire, Lernaean
    Bow, Breastplate of Valor, Hydra''s Lament, Erosion, Pharaoh''s Curse, Eye of
    Providence, Heartseeker, Shogun''s Ofuda, Golden Blade, Shield of the Phoenix,
    Tekko-Kagi, Bragi''s Harp, Rod of Asclepius, Daybreak Gavel, Nimble Ring, Helm
    of Radiance, Midgardian Mail, Triton''s Conch, Stone of Binding, Dominance, Hide
    of the Nemean Lion, Spear of the Magus, Titan''s Bane, Death Metal, Leviathan''s
    Hide, Jade Scepter, The Crusher, Void Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.45
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.45
      pick: 0.0
      fit: 0.37
    Mystical Mail:
      total: 0.65
      efficiency: 0.43
      win: 1.0
      pick: 0.14
      fit: 0.32
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.23
      fit: 0.29
    Soul Reaver:
      total: 0.63
      efficiency: 0.4
      win: 1.0
      pick: 0.14
      fit: 0.26
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.45
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Mystical Mail
  - Freya's Tears
  - Soul Reaver
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Rod of Tahuti
  - Berserker's Shield
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
    this god: Amanita Charm, Berserker''s Shield, Jotunn''s Revenge, Kinetic Cuirass,
    Shield of the Phoenix, Rod of Asclepius, Shield Splitter, Eye of the Storm, Soul
    Gem, Erosion, Ethereal Staff, The Reaper, Breastplate of Valor, Eye of Providence,
    Yogi''s Necklace, Phoenix Feather, Gluttonous Grimoire, Avenging Blade, Pharaoh''s
    Curse, Shogun''s Ofuda, Lernaean Bow, Hydra''s Lament, Lifebinder, Stone of Binding,
    Midgardian Mail, Helm of Radiance, Chandra''s Grace, Daybreak Gavel, Hide of the
    Nemean Lion, Magi''s Cloak, Leviathan''s Hide, Sphere of Negation, Void Shield,
    Stampede, Heartseeker, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.45
      pick: 0.0
      fit: 0.48
    Mystical Mail:
      total: 0.66
      efficiency: 0.43
      win: 1.0
      pick: 0.14
      fit: 0.37
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.23
      fit: 0.37
    Soul Reaver:
      total: 0.63
      efficiency: 0.4
      win: 1.0
      pick: 0.14
      fit: 0.25
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.5
      pick: 0.22
      fit: 0.1
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.84
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Mystical Mail
  - Freya's Tears
  - Soul Reaver
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Gluttonous Grimoire, Berserker''s Shield, Avenging
    Blade, Amanita Charm, Heartseeker, Spear of the Magus, Stone of Binding, Obsidian
    Shard, Spear of Desolation, Tekko-Kagi, Titan''s Bane, Kinetic Cuirass, The Crusher,
    Soul Gem, Void Shield, Screeching Gargoyle, The Reaper, Void Stone, Breastplate
    of Valor, Shield Splitter, Doom Orb, Eye of the Storm, The World Stone, Avatar''s
    Parashu, Hydra''s Lament, Lernaean Bow, Dreamer''s Idol, Pendulum Blade, Nimble
    Ring, Daybreak Gavel, Helm of Radiance, Erosion, Pharaoh''s Curse, Rod of Asclepius,
    Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.45
      pick: 0.0
      fit: 0.56
    Transcendence:
      total: 0.41
      efficiency: 0.53
      win: 0.45
      pick: 0.0
      fit: 0.18
    Mystical Mail:
      total: 0.64
      efficiency: 0.43
      win: 1.0
      pick: 0.14
      fit: 0.22
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.67
      pick: 0.23
      fit: 0.2
    Soul Reaver:
      total: 0.63
      efficiency: 0.4
      win: 1.0
      pick: 0.14
      fit: 0.24
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.22
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Nimble Ring
  - Mystical Mail
  - Freya's Tears
  - Soul Reaver
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
    this god: Berserker''s Shield, Nimble Ring, Golden Blade, Jotunn''s Revenge, Amanita
    Charm, Gluttonous Grimoire, Tyrfing, Riptalon, Kinetic Cuirass, Lernaean Bow,
    Silverbranch Bow, Toxic Blade, Pharaoh''s Curse, Breastplate of Valor, Soul Gem,
    Shogun''s Ofuda, Shield Splitter, Tekko-Kagi, Bragi''s Harp, Eye of the Storm,
    Hydra''s Lament, The Reaper, Daybreak Gavel, Dominance, Avenging Blade, Helm of
    Radiance, Bracer of The Abyss, Rod of Asclepius, Spear of the Magus, Erosion,
    Shield of the Phoenix, Eye of Providence, Qin''s Blade, Vital Amplifier, Heartseeker,
    Obsidian Shard.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.52
      win: 0.45
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.45
      pick: 0.0
      fit: 0.45
    Nimble Ring:
      total: 0.48
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.36
    Mystical Mail:
      total: 0.64
      efficiency: 0.43
      win: 1.0
      pick: 0.14
      fit: 0.21
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.67
      pick: 0.23
      fit: 0.19
    Soul Reaver:
      total: 0.63
      efficiency: 0.4
      win: 1.0
      pick: 0.14
      fit: 0.24
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Mystical Mail
  - Freya's Tears
  - Soul Reaver
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Breastplate of
    Valor, Berserker''s Shield, Amanita Charm, Spear of Desolation, Hydra''s Lament,
    Shield of the Phoenix, Soul Gem, Chronos'' Pendant, Kinetic Cuirass, Screeching
    Gargoyle, Gluttonous Grimoire, Arondight, Nimble Ring, Eye of Erebus, Helm of
    Radiance, Rod of Asclepius, Shield Splitter, Spear of the Magus, Prophetic Cloak,
    Chandra''s Grace, Eye of the Storm, Daybreak Gavel, Obsidian Shard, Erosion, Pharaoh''s
    Curse, Jade Scepter, Lernaean Bow, Eye of Providence, Wish-Granting Pearl, Avenging
    Blade, Totem of Death, Pendulum Blade, Shogun''s Ofuda.'
  slot_scores:
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.45
      pick: 0.0
      fit: 0.49
    Mystical Mail:
      total: 0.64
      efficiency: 0.43
      win: 1.0
      pick: 0.14
      fit: 0.23
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.23
      fit: 0.52
    Soul Reaver:
      total: 0.64
      efficiency: 0.4
      win: 1.0
      pick: 0.14
      fit: 0.3
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.5
      pick: 0.22
      fit: 0.15
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Berserker''s Shield, Amanita Charm,
    Kinetic Cuirass, Shield Splitter, Eye of the Storm, Avenging Blade, Gluttonous
    Grimoire, Lernaean Bow, Breastplate of Valor, Hydra''s Lament, Erosion, Pharaoh''s
    Curse, Eye of Providence, Heartseeker, Shogun''s Ofuda, Golden Blade, Shield of
    the Phoenix, Tekko-Kagi, Bragi''s Harp, Rod of Asclepius, Daybreak Gavel, Nimble
    Ring, Helm of Radiance, Midgardian Mail, Triton''s Conch, Stone of Binding, Dominance,
    Hide of the Nemean Lion, Spear of the Magus, Titan''s Bane, Death Metal, Leviathan''s
    Hide, Jade Scepter, The Crusher, Void Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.45
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.45
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.56
      win: 0.45
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.47
      efficiency: 0.55
      win: 0.45
      pick: 0.0
      fit: 0.51
    Runeforged Hammer:
      total: 0.29
      efficiency: 0.57
      win: 0.0
      pick: 0.22
      fit: 0.56
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.45
  starter: *id001
---
