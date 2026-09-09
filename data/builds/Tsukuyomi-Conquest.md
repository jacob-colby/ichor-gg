---
type: smite-build
god: Tsukuyomi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Mangetsu
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.0
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.3
    win_rate: 0.47
    alternates:
    - name: Transcendence
      pick_rate: 0.3
      win_rate: 0.74
    - name: Hydra's Lament
      pick_rate: 0.16
      win_rate: 0.7
  - name: Hydra's Lament
    pick_rate: 0.27
    win_rate: 0.59
    alternates:
    - name: Transcendence
      pick_rate: 0.21
      win_rate: 0.46
    - name: Book of Thoth
      pick_rate: 0.14
      win_rate: 0.67
  - name: The Crusher
    pick_rate: 0.14
    win_rate: 0.67
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.13
      win_rate: 0.75
    - name: Hydra's Lament
      pick_rate: 0.13
      win_rate: 0.5
  - name: Heartseeker
    pick_rate: 0.33
    win_rate: 0.7
    alternates:
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.6
    - name: Vital Amplifier
      pick_rate: 0.07
      win_rate: 0.25
  - name: Avatar's Parashu
    pick_rate: 0.1
    win_rate: 0.6
    alternates:
    - name: Heartseeker
      pick_rate: 0.13
      win_rate: 0.86
    - name: Titan's Bane
      pick_rate: 0.06
      win_rate: 0.67
  - name: Skeggox
    pick_rate: 0.13
    win_rate: 1.0
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.5
    - name: Blinking Abyss
      pick_rate: 0.06
      win_rate: 0.5
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.33
    win_rate: 0.76
  - name: Bumba's Cudgel
    pick_rate: 0.22
    win_rate: 0.57
  - name: Bluestone Pendant
    pick_rate: 0.1
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/tsukuyomi/
  last_verified: '2026-09-09'
  god_win_rate: 0.5873015873015873
  god_matches_won: 37
  god_matches_played: 63
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-09'
  god_matches_analyzed: 921
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Transcendence
  - Death Metal
  - The Crusher
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - The Crusher
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Death Metal, Tyrfing, Tekko-Kagi, Silverbranch Bow, Lernaean
    Bow, Golden Blade, Nimble Ring, Bragi''s Harp, Titan''s Bane, Spear of the Magus,
    Spear of Desolation, Riptalon, Obsidian Shard, Dominance, Deathbringer, Soul Gem,
    The Reaper, Toxic Blade, Demon Blade, Gluttonous Grimoire, Bracer of The Abyss,
    Musashi''s Dual Swords, Doom Orb, The World Stone, Pendulum Blade, Arondight,
    Runeforged Hammer, Qin''s Blade, Dreamer''s Idol, Damaru, Rage, Ancient Signet,
    Chronos'' Pendant, Avenging Blade, Sun Beam Bow.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.67
      pick: 0.19
      fit: 0.07
    Transcendence:
      total: 0.57
      efficiency: 0.53
      win: 0.74
      pick: 0.3
      fit: 0.24
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.22
      fit: 0.54
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.7
      pick: 0.55
      fit: 0.64
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.27
  community_ordered:
  - Book of Thoth
  - Transcendence
  - The Crusher
  - Heartseeker
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Death Metal
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Book of Thoth
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Death Metal, Spear of Desolation, Nimble Ring, Soul Gem, Spear of the
    Magus, Obsidian Shard, Bragi''s Harp, Tyrfing, Lernaean Bow, Doom Orb, Tekko-Kagi,
    Gluttonous Grimoire, Ancient Signet, The World Stone, Chronos'' Pendant, Titan''s
    Bane, Silverbranch Bow, Dominance, Bracer of The Abyss, Golden Blade, Dreamer''s
    Idol, Deathbringer, The Reaper, Arondight, Gem of Focus, Polynomicon, Pendulum
    Blade, Riptalon, Runeforged Hammer, Musashi''s Dual Swords, Soul Reaver, Rod of
    Asclepius, The Cosmic Horror, Toxic Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.53
      efficiency: 0.51
      win: 0.67
      pick: 0.19
      fit: 0.28
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.47
      pick: 0.3
      fit: 0.52
    Transcendence:
      total: 0.57
      efficiency: 0.53
      win: 0.74
      pick: 0.3
      fit: 0.28
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.54
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.7
      pick: 0.55
      fit: 0.62
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Spear of Desolation
  - Book of Thoth
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Spear of Desolation, Death Metal, Soul Gem, Spear of the Magus,
    Obsidian Shard, Nimble Ring, Silverbranch Bow, Tekko-Kagi, Gluttonous Grimoire,
    Titan''s Bane, Doom Orb, Tyrfing, Lernaean Bow, Bragi''s Harp, The World Stone,
    Chronos'' Pendant, Dreamer''s Idol, The Reaper, Riptalon, Pendulum Blade, Bracer
    of The Abyss, Ancient Signet, Toxic Blade, Golden Blade, Arondight, Gem of Focus,
    Deathbringer, Dominance, The Cosmic Horror, Musashi''s Dual Swords, Runeforged
    Hammer, Rod of Asclepius, Totem of Death, Demon Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.51
      win: 0.67
      pick: 0.19
      fit: 0.16
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.47
      pick: 0.3
      fit: 0.56
    Transcendence:
      total: 0.56
      efficiency: 0.53
      win: 0.74
      pick: 0.3
      fit: 0.16
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.56
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.7
      pick: 0.55
      fit: 0.6
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Berserker's Shield
  - Transcendence
  - Shield of the Phoenix
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Shield of the Phoenix,
    Rod of Asclepius, Kinetic Cuirass, Soul Gem, Golden Blade, Death Metal, The Reaper,
    Riptalon, Runeforged Hammer, Freya''s Tears, Gluttonous Grimoire, Genji''s Guard,
    Breastplate of Valor, Shield Splitter, Ethereal Staff, Yogi''s Necklace, Eye of
    the Storm, Pharaoh''s Curse, Tyrfing, Lernaean Bow, Phoenix Feather, Erosion,
    Nimble Ring, Shogun''s Ofuda, Toxic Blade, Silverbranch Bow, Eye of Providence,
    Spear of the Magus, Lifebinder, Draconic Scale, Tekko-Kagi, Avenging Blade, Helm
    of Radiance, Chandra''s Grace, Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.67
      pick: 0.19
      fit: 0.04
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.42
    Transcendence:
      total: 0.55
      efficiency: 0.53
      win: 0.74
      pick: 0.3
      fit: 0.15
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.6
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.7
      pick: 0.55
      fit: 0.47
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Book of Thoth
  - Transcendence
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  flex_slots:
  - Tekko-Kagi
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Tekko-Kagi, Silverbranch Bow, Spear of the Magus,
    Death Metal, Titan''s Bane, Spear of Desolation, Obsidian Shard, Soul Gem, Riptalon,
    The Reaper, Gluttonous Grimoire, Tyrfing, Toxic Blade, Lernaean Bow, Doom Orb,
    The World Stone, Nimble Ring, Avenging Blade, Dreamer''s Idol, Pendulum Blade,
    Golden Blade, Bragi''s Harp, Dominance, Deathbringer, The Cosmic Horror, Bracer
    of The Abyss, Oath-Sworn Spear, Demon Blade, Musashi''s Dual Swords, The Executioner,
    Runeforged Hammer, Arondight, Ancient Signet, Chronos'' Pendant, Qin''s Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.67
      pick: 0.19
      fit: 0.05
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.47
      pick: 0.3
      fit: 0.6
    Transcendence:
      total: 0.56
      efficiency: 0.53
      win: 0.74
      pick: 0.3
      fit: 0.19
    Tekko-Kagi:
      total: 0.56
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.76
    The Crusher:
      total: 0.58
      efficiency: 0.47
      win: 0.67
      pick: 0.22
      fit: 0.67
    Heartseeker:
      total: 0.62
      efficiency: 0.47
      win: 0.7
      pick: 0.55
      fit: 0.77
  community_ordered:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - The Crusher
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Book of Thoth
  - Transcendence
  - Tyrfing
  - Nimble Ring
  - Heartseeker
  - Riptalon
  flex_slots:
  - Tyrfing
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Nimble Ring, Riptalon, Tyrfing, Silverbranch Bow, Death
    Metal, Soul Gem, Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, Golden Blade,
    The Reaper, Spear of the Magus, Toxic Blade, Bragi''s Harp, Obsidian Shard, Spear
    of Desolation, Dominance, Titan''s Bane, Bracer of The Abyss, Qin''s Blade, Deathbringer,
    Demon Blade, Doom Orb, The World Stone, Ancient Signet, Blood-Bound Book, Sun
    Beam Bow, Dreamer''s Idol, Chronos'' Pendant, Musashi''s Dual Swords, Runeforged
    Hammer, Arondight, Berserker''s Shield, Bancroft''s Talon, Pendulum Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.67
      pick: 0.19
      fit: 0.05
    Transcendence:
      total: 0.55
      efficiency: 0.53
      win: 0.74
      pick: 0.3
      fit: 0.14
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.6
      pick: 0.0
      fit: 0.66
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.39
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.7
      pick: 0.55
      fit: 0.47
    Riptalon:
      total: 0.55
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Book of Thoth
  - Transcendence
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Heartseeker
  - Spear of Desolation
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Spear of Desolation,
    Soul Gem, Death Metal, Chronos'' Pendant, Nimble Ring, Spear of the Magus, Silverbranch
    Bow, Arondight, Gem of Focus, Obsidian Shard, Tyrfing, Lernaean Bow, Pendulum
    Blade, Tekko-Kagi, Gluttonous Grimoire, Bragi''s Harp, Bracer of The Abyss, Titan''s
    Bane, Totem of Death, Doom Orb, Riptalon, Golden Blade, The World Stone, Ancient
    Signet, Breastplate of Valor, Dreamer''s Idol, Deathbringer, Dominance, Toxic
    Blade, Genji''s Guard, The Reaper, Qin''s Blade, Musashi''s Dual Swords, Runeforged
    Hammer, Demon Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.67
      pick: 0.19
      fit: 0.1
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.47
      pick: 0.3
      fit: 0.59
    Transcendence:
      total: 0.55
      efficiency: 0.53
      win: 0.74
      pick: 0.3
      fit: 0.1
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.59
      pick: 0.37
      fit: 0.55
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.7
      pick: 0.55
      fit: 0.44
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Book of Thoth
  - Transcendence
  - Nimble Ring
  - Death Metal
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Nimble Ring
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Rod of Tahuti, Death Metal, Spear of Desolation,
    Soul Gem, Spear of the Magus, Nimble Ring, Obsidian Shard, Bragi''s Harp, Gluttonous
    Grimoire, Chronos'' Pendant, Doom Orb, Silverbranch Bow, Tyrfing, Lernaean Bow,
    Tekko-Kagi, Bracer of The Abyss, The World Stone, Dreamer''s Idol, Ancient Signet,
    Titan''s Bane, Gem of Focus, Golden Blade, The Reaper, Riptalon, Deathbringer,
    Dominance, Arondight, The Cosmic Horror, Pendulum Blade, Rod of Asclepius, Toxic
    Blade, Polynomicon, Totem of Death, Blood-Bound Book, Musashi''s Dual Swords.'
  slot_scores:
    Book of Thoth:
      total: 0.53
      efficiency: 0.51
      win: 0.67
      pick: 0.19
      fit: 0.25
    Transcendence:
      total: 0.56
      efficiency: 0.53
      win: 0.74
      pick: 0.3
      fit: 0.16
    Nimble Ring:
      total: 0.54
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.41
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.54
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.7
      pick: 0.55
      fit: 0.53
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Book of Thoth
  - Transcendence
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Transcendence
  - Death Metal
  - The Crusher
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - The Crusher
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Death Metal, Spear
    of the Magus, Nimble Ring, Spear of Desolation, Obsidian Shard, Bragi''s Harp,
    Soul Gem, Tekko-Kagi, Tyrfing, Lernaean Bow, Gluttonous Grimoire, Silverbranch
    Bow, Titan''s Bane, Doom Orb, Bracer of The Abyss, The World Stone, Golden Blade,
    Dreamer''s Idol, The Reaper, Ancient Signet, Dominance, Deathbringer, Chronos''
    Pendant, Riptalon, Toxic Blade, Musashi''s Dual Swords, Demon Blade, The Cosmic
    Horror, Runeforged Hammer, Arondight, Pendulum Blade, Gem of Focus, Rod of Asclepius,
    Polynomicon.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.67
      pick: 0.19
      fit: 0.22
    Transcendence:
      total: 0.57
      efficiency: 0.53
      win: 0.74
      pick: 0.3
      fit: 0.22
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.59
    The Crusher:
      total: 0.55
      efficiency: 0.47
      win: 0.67
      pick: 0.22
      fit: 0.51
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.7
      pick: 0.55
      fit: 0.61
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Book of Thoth
  - Transcendence
  - The Crusher
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Silverbranch Bow
  - Tekko-Kagi
  - Rod of Tahuti
  flex_slots:
  - Tekko-Kagi
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Death Metal, Tyrfing, Tekko-Kagi, Silverbranch
    Bow, Lernaean Bow, Golden Blade, Nimble Ring, Bragi''s Harp, Spear of the Magus,
    Spear of Desolation, Riptalon, Titan''s Bane, Obsidian Shard, Dominance, Deathbringer,
    Soul Gem, The Reaper, Toxic Blade, Demon Blade, Gluttonous Grimoire, Bracer of
    The Abyss, Musashi''s Dual Swords, Doom Orb, The World Stone, Pendulum Blade,
    Arondight, Runeforged Hammer, Qin''s Blade, Dreamer''s Idol, Damaru, Rage, Ancient
    Signet, Chronos'' Pendant, Avenging Blade, Sun Beam Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.47
      pick: 0.3
      fit: 0.49
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.6
      pick: 0.0
      fit: 0.72
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.58
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.69
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.27
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
