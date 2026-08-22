---
type: smite-build
god: Danzaburou
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fellowship
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.62
  slot_order:
  - name: Transcendence
    pick_rate: 0.3
    win_rate: 0.65
    alternates:
    - name: Tyrfing
      pick_rate: 0.11
      win_rate: 0.32
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.56
  - name: Jotunn's Revenge
    pick_rate: 0.16
    win_rate: 0.68
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.11
      win_rate: 0.48
    - name: Book of Thoth
      pick_rate: 0.1
      win_rate: 0.71
  - name: The World Stone
    pick_rate: 0.13
    win_rate: 0.73
    alternates:
    - name: Polynomicon
      pick_rate: 0.06
      win_rate: 0.59
    - name: Silverbranch Bow
      pick_rate: 0.06
      win_rate: 0.36
  - name: Rod of Tahuti
    pick_rate: 0.1
    win_rate: 0.61
    alternates:
    - name: The Executioner
      pick_rate: 0.09
      win_rate: 0.45
    - name: Silverbranch Bow
      pick_rate: 0.08
      win_rate: 0.6
  - name: Heartseeker
    pick_rate: 0.05
    win_rate: 0.57
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.47
    - name: Polynomicon
      pick_rate: 0.05
      win_rate: 0.64
  - name: Manchu Bow
    pick_rate: 0.05
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.85
    - name: Titan's Bane
      pick_rate: 0.04
      win_rate: 0.44
  community_starters:
  - name: Conduit Gem
    pick_rate: 0.15
    win_rate: 0.52
  - name: Archmage's Gem
    pick_rate: 0.14
    win_rate: 0.58
  - name: Sharpshooter's Arrow
    pick_rate: 0.1
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/danzaburou/
  last_verified: '2026-08-22'
  god_win_rate: 0.5459770114942529
  god_matches_won: 190
  god_matches_played: 348
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-22'
  god_matches_analyzed: 14126
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Death Metal, Berserker''s Shield, Gluttonous Grimoire,
    The Crusher, Soul Gem, Riptalon, Lernaean Bow, Silverbranch Bow, Tekko-Kagi, The
    Reaper, Golden Blade, Bragi''s Harp, Spear of the Magus, Deathbringer, Damaru,
    Runeforged Hammer, Hydra''s Lament, Spear of Desolation, Obsidian Shard, Heartseeker,
    Dominance, Genji''s Guard, Demon Blade, Breastplate of Valor, Toxic Blade, Pharaoh''s
    Curse, Amanita Charm, Bracer of The Abyss, Kinetic Cuirass, Musashi''s Dual Swords,
    Shogun''s Ofuda, Freya''s Tears, Shield Splitter, Helm of Radiance, Doom Orb,
    Eye of Providence, Avenging Blade, Titan''s Bane, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.51
      win: 0.71
      pick: 0.14
      fit: 0.05
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.68
      pick: 0.22
      fit: 0.37
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.65
      pick: 0.3
      fit: 0.18
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.61
      pick: 0.17
      fit: 0.2
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Death Metal
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire, Berserker''s Shield, The Crusher,
    Spear of Desolation, Spear of the Magus, Hydra''s Lament, Genji''s Guard, Breastplate
    of Valor, Obsidian Shard, Bragi''s Harp, Lernaean Bow, The Reaper, Runeforged
    Hammer, Tekko-Kagi, Golden Blade, Heartseeker, Silverbranch Bow, Doom Orb, Ancient
    Signet, Riptalon, Helm of Radiance, Bracer of The Abyss, Chronos'' Pendant, Dominance,
    Amanita Charm, Freya''s Tears, The Cosmic Horror, Deathbringer, Damaru, Ethereal
    Staff, Kinetic Cuirass, Rod of Asclepius, Bancroft''s Talon, Wish-Granting Pearl,
    Titan''s Bane, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.54
      efficiency: 0.51
      win: 0.71
      pick: 0.14
      fit: 0.24
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.68
      pick: 0.22
      fit: 0.44
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.65
      pick: 0.3
      fit: 0.24
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.51
    The World Stone:
      total: 0.57
      efficiency: 0.52
      win: 0.73
      pick: 0.2
      fit: 0.35
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.61
      pick: 0.17
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Damaru
  - The World Stone
  - Deathbringer
  - Rod of Tahuti
  flex_slots:
  - Deathbringer
  - Damaru
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Death Metal, Nimble Ring, Berserker''s Shield, Gluttonous Grimoire,
    Soul Gem, The Crusher, Riptalon, Silverbranch Bow, Lernaean Bow, The Reaper, Tekko-Kagi,
    Golden Blade, Deathbringer, Damaru, Spear of the Magus, Spear of Desolation, Obsidian
    Shard, Bragi''s Harp, Runeforged Hammer, Genji''s Guard, Breastplate of Valor,
    Demon Blade, Hydra''s Lament, Heartseeker, Amanita Charm, Dominance, Musashi''s
    Dual Swords, Toxic Blade, Pharaoh''s Curse, Kinetic Cuirass, Bracer of The Abyss,
    Shogun''s Ofuda, Freya''s Tears, Helm of Radiance, Doom Orb, The Cosmic Horror,
    Eye of Providence, Shield Splitter, Titan''s Bane, Tyrfing.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.68
      pick: 0.22
      fit: 0.34
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.49
    Damaru:
      total: 0.51
      efficiency: 0.5
      win: 0.6
      pick: 0.0
      fit: 0.44
    The World Stone:
      total: 0.55
      efficiency: 0.52
      win: 0.73
      pick: 0.2
      fit: 0.2
    Deathbringer:
      total: 0.51
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.61
      pick: 0.17
      fit: 0.2
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Nimble Ring, Death Metal, Spear of Desolation,
    The Crusher, Berserker''s Shield, Spear of the Magus, Obsidian Shard, Silverbranch
    Bow, The Reaper, Riptalon, Genji''s Guard, Breastplate of Valor, Tekko-Kagi, Hydra''s
    Lament, Lernaean Bow, Bragi''s Harp, Heartseeker, Freya''s Tears, Doom Orb, The
    Cosmic Horror, Golden Blade, Runeforged Hammer, Chronos'' Pendant, Amanita Charm,
    Helm of Radiance, Bracer of The Abyss, Dreamer''s Idol, Kinetic Cuirass, Toxic
    Blade, Deathbringer, Damaru, Ancient Signet, Ethereal Staff, Shield of the Phoenix,
    Rod of Asclepius, Titan''s Bane, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.71
      pick: 0.14
      fit: 0.13
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.68
      pick: 0.22
      fit: 0.46
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.65
      pick: 0.3
      fit: 0.13
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.37
    The World Stone:
      total: 0.57
      efficiency: 0.52
      win: 0.73
      pick: 0.2
      fit: 0.33
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.61
      pick: 0.17
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The World Stone
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - The World Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Soul Gem, Shield of the Phoenix,
    The Reaper, Riptalon, Kinetic Cuirass, Gluttonous Grimoire, Ethereal Staff, Rod
    of Asclepius, Nimble Ring, Death Metal, Pharaoh''s Curse, Runeforged Hammer, Golden
    Blade, Freya''s Tears, The Crusher, Genji''s Guard, Blood-Bound Book, Breastplate
    of Valor, Yogi''s Necklace, Shogun''s Ofuda, Phoenix Feather, Shifter''s Shield,
    Shield Splitter, Chandra''s Grace, Bancroft''s Talon, Lernaean Bow, Silverbranch
    Bow, Mantle Of Discord, Stone of Binding, Spectral Armor, Eye of the Storm, Spear
    of the Magus, Lifebinder, Tekko-Kagi, Erosion, Helm of Radiance, Leviathan''s
    Hide, Tyrfing.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.68
      pick: 0.22
      fit: 0.25
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.43
    The World Stone:
      total: 0.54
      efficiency: 0.52
      win: 0.73
      pick: 0.2
      fit: 0.14
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - The World Stone
  - Rod of Tahuti
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, The Crusher, Soul Gem, Nimble Ring, Silverbranch
    Bow, Riptalon, Death Metal, The Reaper, Tekko-Kagi, Berserker''s Shield, Spear
    of the Magus, Obsidian Shard, Spear of Desolation, Avenging Blade, Heartseeker,
    Stone of Binding, Lernaean Bow, Toxic Blade, Screeching Gargoyle, Golden Blade,
    Doom Orb, The Cosmic Horror, Runeforged Hammer, Genji''s Guard, Breastplate of
    Valor, Hydra''s Lament, Dreamer''s Idol, Bragi''s Harp, Amanita Charm, Deathbringer,
    Damaru, Avatar''s Parashu, Kinetic Cuirass, Void Shield, Dominance, Pharaoh''s
    Curse, Pendulum Blade, Titan''s Bane, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.51
      win: 0.71
      pick: 0.14
      fit: 0.04
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.68
      pick: 0.22
      fit: 0.48
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.65
      pick: 0.3
      fit: 0.15
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.32
    The World Stone:
      total: 0.57
      efficiency: 0.52
      win: 0.73
      pick: 0.2
      fit: 0.35
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.61
      pick: 0.17
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Book of Thoth
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Silverbranch Bow
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Berserker''s Shield, Death Metal, Silverbranch Bow, Riptalon,
    Gluttonous Grimoire, Golden Blade, Soul Gem, The Crusher, Lernaean Bow, Tekko-Kagi,
    The Reaper, Toxic Blade, Spear of the Magus, Genji''s Guard, Breastplate of Valor,
    Runeforged Hammer, Bragi''s Harp, Obsidian Shard, Spear of Desolation, Amanita
    Charm, Hydra''s Lament, Pharaoh''s Curse, Deathbringer, Damaru, Kinetic Cuirass,
    Dominance, Bracer of The Abyss, Heartseeker, Shogun''s Ofuda, Qin''s Blade, Freya''s
    Tears, Demon Blade, Eye of Providence, Helm of Radiance, Musashi''s Dual Swords,
    Shield Splitter, Doom Orb, Titan''s Bane, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.51
      win: 0.71
      pick: 0.14
      fit: 0.04
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.68
      pick: 0.22
      fit: 0.28
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.65
      pick: 0.3
      fit: 0.13
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.36
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.13
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Book of Thoth
  - Transcendence
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Nimble Ring, Spear of Desolation,
    Genji''s Guard, Breastplate of Valor, Death Metal, Berserker''s Shield, Gluttonous
    Grimoire, Hydra''s Lament, Freya''s Tears, Chronos'' Pendant, The Crusher, Shield
    of the Phoenix, Silverbranch Bow, Spear of the Magus, Riptalon, Lernaean Bow,
    Screeching Gargoyle, Obsidian Shard, The Reaper, Arondight, Gem of Focus, Amanita
    Charm, Golden Blade, Tekko-Kagi, Kinetic Cuirass, Runeforged Hammer, Bragi''s
    Harp, Totem of Death, Bracer of The Abyss, Helm of Radiance, Pharaoh''s Curse,
    Pendulum Blade, Deathbringer, Damaru, Heartseeker, Eye of Providence, Chandra''s
    Grace, Doom Orb, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.71
      pick: 0.14
      fit: 0.08
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.68
      pick: 0.22
      fit: 0.48
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.65
      pick: 0.3
      fit: 0.08
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.61
      pick: 0.17
      fit: 0.2
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Nimble Ring, Soul Gem, Death Metal, Gluttonous
    Grimoire, Spear of Desolation, Berserker''s Shield, Spear of the Magus, Obsidian
    Shard, The Crusher, Bragi''s Harp, Genji''s Guard, Breastplate of Valor, Silverbranch
    Bow, Lernaean Bow, The Reaper, Riptalon, Hydra''s Lament, Bracer of The Abyss,
    Chronos'' Pendant, Helm of Radiance, Tekko-Kagi, Doom Orb, The Cosmic Horror,
    Golden Blade, Runeforged Hammer, Ancient Signet, Freya''s Tears, Ethereal Staff,
    Rod of Asclepius, Amanita Charm, Blood-Bound Book, Dreamer''s Idol, Kinetic Cuirass,
    Heartseeker, Deathbringer, Damaru, Gem of Focus, Titan''s Bane, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.53
      efficiency: 0.51
      win: 0.71
      pick: 0.14
      fit: 0.2
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.68
      pick: 0.22
      fit: 0.38
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.65
      pick: 0.3
      fit: 0.13
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.45
    The World Stone:
      total: 0.57
      efficiency: 0.52
      win: 0.73
      pick: 0.2
      fit: 0.34
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.61
      pick: 0.17
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Death Metal, Nimble Ring, Gluttonous
    Grimoire, Soul Gem, Berserker''s Shield, The Crusher, Spear of the Magus, Obsidian
    Shard, Spear of Desolation, Bragi''s Harp, The Reaper, Lernaean Bow, Tekko-Kagi,
    Silverbranch Bow, Riptalon, Golden Blade, Runeforged Hammer, Bracer of The Abyss,
    Hydra''s Lament, Helm of Radiance, Heartseeker, Doom Orb, The Cosmic Horror, Genji''s
    Guard, Deathbringer, Damaru, Breastplate of Valor, Amanita Charm, Ancient Signet,
    Dominance, Ethereal Staff, Dreamer''s Idol, Kinetic Cuirass, Blood-Bound Book,
    Rod of Asclepius, Chronos'' Pendant, Pharaoh''s Curse, Titan''s Bane, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.53
      efficiency: 0.51
      win: 0.71
      pick: 0.14
      fit: 0.18
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.68
      pick: 0.22
      fit: 0.36
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.65
      pick: 0.3
      fit: 0.18
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.45
    The World Stone:
      total: 0.57
      efficiency: 0.52
      win: 0.73
      pick: 0.2
      fit: 0.33
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.61
      pick: 0.17
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Berserker's Shield
  - Gluttonous Grimoire
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Nimble Ring, Death Metal, Berserker''s Shield, Gluttonous
    Grimoire, The Crusher, Soul Gem, Riptalon, Lernaean Bow, Tekko-Kagi, Tyrfing,
    The Reaper, Golden Blade, Silverbranch Bow, Heartseeker, Bragi''s Harp, Spear
    of the Magus, Deathbringer, Damaru, Runeforged Hammer, Hydra''s Lament, Spear
    of Desolation, Obsidian Shard, Dominance, Genji''s Guard, Demon Blade, Breastplate
    of Valor, Titan''s Bane, Toxic Blade, Pharaoh''s Curse, Amanita Charm, Bracer
    of The Abyss, Kinetic Cuirass, Musashi''s Dual Swords, Shogun''s Ofuda, Freya''s
    Tears, Shield Splitter, Helm of Radiance, Doom Orb, Eye of Providence, Avenging
    Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.68
      pick: 0.22
      fit: 0.37
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.61
      pick: 0.17
      fit: 0.2
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Death Metal
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - The World Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Nimble Ring, Death Metal, Berserker''s
    Shield, Gluttonous Grimoire, The Crusher, Soul Gem, Riptalon, Lernaean Bow, Tekko-Kagi,
    Tyrfing, The Reaper, Golden Blade, Silverbranch Bow, Heartseeker, Bragi''s Harp,
    Spear of the Magus, Deathbringer, Damaru, Runeforged Hammer, Hydra''s Lament,
    Spear of Desolation, Obsidian Shard, Dominance, Genji''s Guard, Demon Blade, Breastplate
    of Valor, Titan''s Bane, Toxic Blade, Pharaoh''s Curse, Amanita Charm, Bracer
    of The Abyss, Kinetic Cuirass, Musashi''s Dual Swords, Shogun''s Ofuda, Freya''s
    Tears, Shield Splitter, Helm of Radiance, Doom Orb, Eye of Providence, Avenging
    Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.68
      pick: 0.22
      fit: 0.37
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.65
      pick: 0.3
      fit: 0.18
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.48
    The World Stone:
      total: 0.55
      efficiency: 0.52
      win: 0.73
      pick: 0.2
      fit: 0.2
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.61
      pick: 0.17
      fit: 0.2
  swaps:
  - added: The World Stone
    removed: Gluttonous Grimoire
    reason: community 73% win over 45 matches (vs 55% on this god), taking the model's
      weakest slot from Gluttonous Grimoire
  - added: Transcendence
    removed: Berserker's Shield
    reason: community 65% win over 104 matches (vs 55% on this god), taking the model's
      weakest slot from Berserker's Shield
  starter: *id001
---
